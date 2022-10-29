![GitHub](https://img.shields.io/github/license/hunar4321/life_code)

# Discord-Asciifier
A script I wrote for a discord bot to convert images into text. The code is somewhat messy as most my projects tend to be. I didn't feel that polishing it was worth the time I could spend learning to do something else. 

To use, just copy the script, install the python libraries used, and run it. Explanation on how to change the settings of the ascii generator are in the script when you run it. Default size is ~2000 characters because that is discord's character limit per message (It usually doesn't look great). If you pick a size more than 1, it will multiply the number of characters available to the script by that number. I recommend picking size 3 for pretty images.

Code is pretty simple. It takes an image, compresses it to a certain size, then goes through the image pixel-by-pixel and determines which character to use in its place based on the brightness. The image won't look right unless you view it with a monospace font.

Do what you want with the code, but credit would be much appreciated. Contact info in the profile.

Here is an example:
------------------------

```
                                                                #####                                       
                                                               ########?                                    
                                                              ############                                  
                                                              :############# %####                          
                                                               ######################                       
                                                              ########################%                     
                                                          ##############################                    
                                                        ################################                    
                                                      +##################################                   
                                                     #####################################                  
                                                     #####################################:                 
                                                    #######################################                 
                                                    ########################################                
                                                    %#######################################                
                                                    ?#######################################%               
                                                      #######################################               
                                                         :###################################               
                                                          ###################################               
                                                         ####################################+              
                                                           ##################################%              
                                                             #################################              
                                                              ################################              
                                                              %##### #########################              
                                       %#####                  ###############################              
                                  ?###########:                ##########################+####              
                                 ##############                 ######################### ####              
                                :##############                 ######################## ? # %              
                                 ##############                #########################    :               
                                 ###############?              ###################### ##                    
                                  #################      ############################# ##                   
                                   :#################     ############################                      
                                       %###############  ##############################                     
                                         ##############################################                     
                                        ###############################################:                    
                                       +################################################                    
                                       #################################################     ?##            
                                       #################################################%######             
                                       ####################################################                 
                                      %######################+############################%                 
                                      ####################### #############################                 
```
![2022-08-31_12-16](https://user-images.githubusercontent.com/96934612/187763827-db23a1a8-0154-4ff4-8b25-74f5bc74544c.jpg)

PS: You might or might not be able to use this to animate things on discord with bots. Allegedly somebody did that and it looked pretty good, hypothetically speaking.
