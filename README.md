
# FFMPEG Video Tools

A django project to perform video manipulations using FFMPEG


## Installation 

Clone the project and install all the required packages by running following command
```bash
  pip install -r requirements.txt
```

### RabbitMQ and Erlang

**NOTE:** _Following installation steps are for Windows OS, if you wannt to install it on Debain/Ubuntu follow the steps mentioned [here](https://www.rabbitmq.com/install-debian.html#apt-cloudsmith)_

For installing RabbitMQ on windows we need to install Erlang 1st.

Erlang installer can be downloaded from [here](https://erlang.org/download/otp_versions_tree.html). Once downloaded install it as administrator with default settings.

Once Erlang is installed you can donwload RabbitMQ official installer from [here](https://rabbitmq.com/install-windows.html#downloads). Install RabbitMQ as administrator with default settings.

### FFMPEG

FFMPEG build can be installed from gyan.dev

1. Download the latest full build from [here](https://www.gyan.dev/ffmpeg/builds/)
2. Unzip this file by using any file archiver such as Winrar or 7z.
3. Rename the extracted folder to ffmpeg and move it into the root of C: drive.
4. Now, run cmd as an administrator and set the environment path variable for ffmpeg by running the following command:
```bash
  setx /m PATH "C:\ffmpeg\bin;%PATH%"
``` 
5. To verify the installation close and open a new command prompt and run the following command:
```bash
  ffmpeg -version
```

### Email Settings

Email settings needs to be updated as per the user preference. EMAIL_HOST_PASSWORD in VideoTools.settings.py must be updated with the App password of the EMAIL_HOST_USER

## Run Locally

Go to the project directory

```bash
  cd ffmpeg-videotools
```

Start the Django server

```bash
  python manage.py runserver
```

Start the RabbitMQ

- Search windows for "RabbitMQ Service - start" and run it as administrator

Start the Celery

- Run the following command in a new command prompt to start celery

```bash
  celery -A VideoTools worker -l INFO --pool=solo
```

## API Reference

#### Blur Video

```http
  POST /blur/
```

| Parameter            | Type     | Description                      |
| :--------            | :------- | :-------------------------       |
| `timestamps`         | `list`   | **Required**. List of timestamps to be blurred |
| `notification_email` | `string` | **Required**. Email id to which a notification <br />will be triggered once the job is done |
| `file_path`          | `string` | **Required**. Path of the file to input video. <br />This can be a path to local file or a hosted URL |


## Demo

https://user-images.githubusercontent.com/46415067/192385904-9456eac6-7252-4425-bb8f-d819b12da04b.mp4


## License

[MIT](https://choosealicense.com/licenses/mit/)
