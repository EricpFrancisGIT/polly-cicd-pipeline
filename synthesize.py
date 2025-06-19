import boto3
import os

def synthesize_speech(text, output_file):
    
    polly = boto3.client('polly')

    response = polly.synthesize_speech(
        Text=text,
        OutputFormat='mp3',
        VoiceId='Stephen'
        Engine='neural'
    )

    with open(output_file, 'wb') as file:
        file.write(response['AudioStream'].read())

    print(f"Audio content written to file {output_file}")



def upload_to_s3(file_path, bucket_name, object_key):

    s3 = boto3.client('s3')

    s3.upload_file(file_path, bucket_name, object_key)
    print(f"The file has been uploaded to s3://{bucket_name}/{object_key}")



def main ():

    bucket_name = os.environ.get('S3_BUCKET_NAME')
    output_file = os.environ.get('OUTPUT_FILE', 'output.mp3')
    object_key = f'pixel-polly-audio/{output_file}'

    with open('speech.txt', 'r') as file:
        text = file.read()

        synthesize_speech(text, output_file)

        upload_to_s3(output_file, bucket_name, object_key)

if __name__ == "__main__":
    main() 
