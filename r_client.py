import pyRserve

class RClient:
    
    def __init__(self):
        self.R_conn = pyRserve.connect()

    def predict_species(self, sl, sw, pl, pw):
        return self.R_conn.eval('predict_species(%f, %f, %f, %f)' % (sl, sw, pl, pw))

    def predict_attribute(self, predict_attr, species, sl, sw, pl, pw):
        lst = [predict_attr, species, sl, sw, pl, pw]
        str_lst = map(lambda(x) : str(x) if x != 0 else 'NULL', lst)
        predict_attr, species, sl, sw, pl, pw = str_lst
        predict_attr = '"' + predict_attr + '"'
        species = '"' + species + '"'
        return self.R_conn.eval('predict_attribute(%s, %s, %s, %s, %s, %s)' %(predict_attr, species, sl, sw, pl, pw))

    def shutdown(self):
        self.R_conn.shutdown()

