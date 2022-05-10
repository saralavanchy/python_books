import datetime
import jwt

def getJWT(userId: number):
    timeLimit= datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    payload = {"user_id": userId ,"exp":timeLimit}
    
    return jwt.encode(payload, "super-secret-other-aaa")

configs = {
    "username":"sara",
    "password":"1234"
}


# Using of pickle/c_pickle/_pickle with load/loads:
import pickle
data = """ cos.system(S'dir')tR. """
pickle.loads(data)

###

# Using PyYAML with load:
import yaml
document = "!!python/object/apply:os.system ['ipconfig']"
print(yaml.load(document))

AWS_SECRET_ACCESS_KEY = '1111'
