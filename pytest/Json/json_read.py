import logging
from io import StringIO
import json

fileObj = StringIO()
json.dump(["Hello", "Geeks"], fileObj)
logging.info("Using json.dump(): " + str(fileObj.getvalue()))


# Encoding is covert python object as json string
class TypeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, type):
            return str(obj)


logging.info("Using json.dumps(): " + str(json.dumps(type(str), cls=TypeEncoder)))
logging.info("Using json.JSONEncoder().encode" +
             str(TypeEncoder().encode(type(list))))
logging.info("Using json.JSONEncoder().iterencode" +
             str(list(TypeEncoder().iterencode(type(dict)))))
