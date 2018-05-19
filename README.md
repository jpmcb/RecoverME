# RecoverME
CS 361 - Basic implementation and skeleton for the RecoverME application

## Set up local dev enviroment:
1. Pull from this githup repo
2. Install the local node modules using `npm install`
- This will install the needed view and engine modules to run the app
3. Start the application with `node server.js`
- You may now navigate to a locally running version of the application at `localhost:3000`


## Basic skeleton of the App:

1. `server.js` is the entry point for the node app. Any route handlers or various server logic should go here.
2. `public` holds the various static resources for the app (CSS, images, etc). To access these resources, ensure that the full file path is specified (see main.handlebars for an example)
3. `views` holds the various handlebars views that can be dynamically generated


## To add a node module:
1. Install the module using `npm install <MODULE NAME>`
2. `require` the node module in server.js
3. Use the various modules components