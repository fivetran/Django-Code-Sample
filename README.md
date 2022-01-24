# About
Uplift on the current vandelay demo page. [Where do I recognize this name from](https://seinfeld.fandom.com/wiki/Vandelay_Industries)?


# 📣 Prerequisite

## Have the right packages installed in your local environment
* Make sure you have [brew](https://brew.sh/) installed
* Make sure you have pip installed (comes with [Python 3 installation via Brew](https://docs.python-guide.org/starting/install3/osx/))
* Make sure you have virtualenv installed (`pip install virtualenv`)
* Make sure you have [node](https://nodejs.org/en/) installed
* Make sure you're using Python 3 `python --version` or `python3 --version`

## Have a working destination synced in your Fivetran account
Go to your Fivetran account and setup a destination via the UI. This will assign you a `group_id` which you should be able to gather from the following steps:

1. Go to https://fivetran.com/warehouses and select your warehouse
2. Navigate to the `Destination` tab and select the destination that you setup in the prerequisite step
3. Navigate to the `Connection Details` area and scroll down to where it says `Destination Group ID` to see your value.
4. Copy this value down as it is very important for a live, data flowing, application.


# 🏃 Quickstart

## 0. Create a new directory in your development directory environment
```
$ cd Desktop/dev
$ mkdir PBFDemo && cd PBFDemo
```

## 1. Clone this repository into the previously created directory
 ```
 $ cd PBFDemo && git clone https://github.com/fivetran-connorbrereton/Django-Code-Sample.git
 $ cd Django-Code-Sample
 ```
 
## 2. Navigate to the directory where the `settings.py` file lives and create an environment variable file
 ```
 $ cd vandelay_project/vandelay_project
 $ touch .env
 <open the .env file using your favorite text editor>
 ```
 
## 3. Add in your API_KEY and API_SECRET from your Fivetran account preferences
 Note that it is *crucial* you use the exact same format as seen below as this file is case sensitive.
 ```
 API_KEY=<YOUR_API_KEY>
 API_SECRET=<YOUR_API_SECRET>
 ```
To avoid any issues just copy and paste the code above into your own `.env` file. Make sure you replace the temporary variables with your own API_KEY and API_SECRET.

## 4. Add your Group ID to the `parameters.py` file in the Django project
The `parameters.py` file is located in the following directory: `Django-Code-Sample/vandelay_project/vandelay_app`. You just need to go to **line 11** and place in your string value for the Group ID.

## 5. Add your Group ID to the `app_funcs.py` flie in the Django project
The `app_funcs.py` file is located in the following directory: `Django-Code-Sample/vandelay_project/vandelay_app`. You just need to go to **line 9** and place in your string value for the Group ID in the 1st index. Do not touch the 0th index please :)

## 6. Navigate to the root folder of the project directory and run the shell script to get the demo environment installed and started
```
$ cd ../..
$ ./setup.sh
```

## 7. Exit tailwind and render the Django view.
Hit `CTRL-C` to exit the tailwind server and return to the Django server page being rendered.

## 8. Open the demo app in your browser.
Go to `localhost:8000` and view the rendered application.

# ‼️ Important Notes ‼️
- When you setup the demo environment you can only use one instance of each connector. If you click on the connector multiple times you will be promted with the following error:
```
Error occured - Failed while posting on https://api.fivetran.com/v1/connectors {"code":"SchemaExists","message":"An integration with schema \"test_oracle\" already exists, please choose a different schema"}
```

- The only way to resolve this error is to go to the `Connectors` section of your Fivetran Dashboard and delete the already existing instance of the connector you're trying to configure.

- After deleting the connector retry the connector creation flow and be patient with the process. In your terminal you will see a payload that looks like (below) this when the request has finished rendering. You will shortly see the UI render after this response body has been posted to standard output.
```
[03/Nov/2021 17:45:36] "GET /pbf/connect-card/?service=oracle_rds HTTP/1.1" 200 528
{"code":"Success","message":"Connector has been created", ...
...
```


### 🙋 I'm having problems!
* Inspect your console and see if it says it can't find the CSS file. If that's true, try and restart the tailwind service (which generates the css file), then restart the django server so it detects the file. That should do it. 

Then, navigate to the server in your browser at localhost:8000 😊

All files will automatically reload when they're changed via browsersync. If you want to adjust the base styling, it's in `vandelay_project/theme/templates`.

Available URLs:
- Vandelay Demo: http://127.0.0.1:8000/pbf/
