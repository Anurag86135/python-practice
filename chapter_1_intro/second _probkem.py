# question 3.) Install an external module and use it to perform an operation of your interest
import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("mera naam  kya karega jaan kar bee")
engine.runAndWait()