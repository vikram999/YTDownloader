steps to deploy streamlit app in Heroku

=> StreamLit App Ready 
=> Github Account 
=> Heroku Account 

=> Create setup.sh File => This shell script will tell Heroku Server to run our StreamLit app 
                        => This will have commands  of streamLit 
=> ProcFile => ProcFIle is for Heroku ,When you deploy your code , 
				Heroku Needs to understand starting point of your code 	
                => web: sh setup.sh && streamlit run app.py  
                this is the command -> app.py is our main file ,app File

=> requirements.txt => It will have all the Libraries we need (No Import and any key word, just library names)
                    => Each in next Line				