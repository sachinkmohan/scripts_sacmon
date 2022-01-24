

#Another way of writing a main program in python

def main():
    try:
        while True:
            print("Camera test")
            
            
    except KeyboardInterrupt:
        pass
    
if __name__ == "__main__":
    main()



v4l2-ctl --list-devices -> will give you list of video devices connected including dummy
