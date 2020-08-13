import bcrypt

class SaltService():

    def GetHashedPassword(self,passw):
        return bcrypt.hashpw(passw, bcrypt.gensalt())

    def ValidatePassword(self, passw, hashed):
        return bcrypt.checkpw(passw, hashed)

