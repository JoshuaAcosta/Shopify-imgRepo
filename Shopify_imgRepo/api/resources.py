"""API """
import os
from flask_restful import Resource, fields, marshal
from flask_login import current_user
from flask import request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from Shopify_imgRepo.models import Image
from Shopify_imgRepo import db
import boto3

AWS_BUCKET_NAME = os.environ.get('AWS_BUCKETNAME')
AWS_ACCESS_KEY_ID= os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY= os.environ.get('AWS_SECRET_ACCESS_KEY')
ALLOWED_EXTENSIONS = ('.png', '.jpg', '.jpeg')

get_image_fields = {
    "image_id": fields.Integer,
    "file_name": fields.String,
    "file_location": fields.String,
    "user_id": fields.Integer
}

get_401_fields = {
    "response": fields.String
}

def allowed_file(filename):
    """ helper function checks if the filename extension is allowed """
    file_ext = os.path.splitext(filename)
    return True if file_ext[1] in ALLOWED_EXTENSIONS else False

class ImageResources(Resource):
    """HTTP API methods regarding current user's images"""
    def get(self):
        """Returns all images for user to be displayed"""
        if current_user.is_authenticated:
            id_num = current_user.get_id()
            return  marshal(Image.query.filter_by(user_id=id_num).all(), get_image_fields), 200
        else:
            response = {'response':'Unauthenticated. Please log in'}
            return marshal(response, get_401_fields), 401


    def post(self):
        """Store new image in AWS S3 and image data in db"""
        if (current_user.is_authenticated) and (request.method == 'POST'):
            user_id = current_user.get_id()
            
            if 'file' not in request.files:
                flash("No file part", "error")
                return redirect(url_for('main.galeria'))

            img_file = request.files["file"]

            if img_file.filename == '':
                flash("No image selected", "error")
                return redirect(url_for('main.galeria'))

            if img_file:
                file_name = secure_filename(img_file.filename)

                if not allowed_file(file_name):
                    flash("Only .jpg, .jpeg and .png are allowed at the moment", "error")
                    return redirect(url_for('main.galeria'))

                img_file.save(file_name)
                object_name = f"{user_id}/{file_name}"
                file_S3location = f"https://{AWS_BUCKET_NAME}.s3.amazonaws.com/{object_name}"

                s3_client = boto3.client('s3',
                                    aws_access_key_id=AWS_ACCESS_KEY_ID,
                                    aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
                s3_client.upload_file(file_name, AWS_BUCKET_NAME, object_name)

                new_image = Image(
                    file_name= file_name,
                    file_location=file_S3location,
                    user_id=user_id
                    )
                db.session.add(new_image)
                db.session.commit()

            flash("Upload successful!", "success")
            return redirect(url_for('main.galeria'))
        else:
            response = {'response':'Unauthenticated. Please log in'}
            return marshal(response, get_401_fields), 401