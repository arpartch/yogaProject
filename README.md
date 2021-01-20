Move to the root direcotry of the project
```cd myproject```
Invoke the virtual environment to make sure we are running python 3.7
```. venv/bin/activate```
Export the enviornment setting development so flask automatically reloads when I make changes
```export FLASK_ENV=development```
Export server.py as the app so flask run know what file to run
```export FLASK_APP=server.py```
Invoke flask with the command run to start a running instance of my API server
```flask run```
Confirm that API is running by browsing to http://127.0.0.1:5000/users/peter
```Second Terminal```
cd into my-app
yarn start