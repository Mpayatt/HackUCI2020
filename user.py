class User:
    def __init__(self, name: str, phoneNumber: str, progress: int, contacts: [str]):
        self._name = name
        self._phoneNumber = phoneNumber
        self._progress = progress
        self._contacts = contacts

    def getName(self)->str:
        return self._name 

    def getProgress(self)->int:
        return self._progress

    def getUserNumber(self)->str:
        return self._userNumber

    def getContacts(self)->[str]:
        return self._contacts

    def getPhoneNumber(self)->str:
        return self._phoneNumber

    def setProgress(self, newProgress):
        self._progress = newProgress

    def setName(self, newName):
        self._name = newName

    def addContact(self, phoneNumber: str):
        self._contacts.append(phoneNumber)

    def __repr__:
        return "User(name={}, phoneNumber={}, progress={}, contacts={})".format(self._name, self._phoneNumber, self._progress, self._contacts)

    def to_dict(self):
        dest = {
            u'name' : self._name
            u'phoneNum': self._phoneNumber
            u'progress': self._progress
            u'contacts': self._contacts
        }

        return dest

    @staticmethod
    def from_dict(source):
        user = User(source[u'name'], source[u'phoneNumber'], source[u'progress'], source[u'contacts'])

        return user
