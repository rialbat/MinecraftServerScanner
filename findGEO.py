from pysyge.pysyge import GeoLocator, MODE_BATCH, MODE_MEMORY

class FindGEO:

    def __init__(self, ip):
        self._geodata = GeoLocator('SxGeoCity.dat', MODE_BATCH | MODE_MEMORY)
        self._ipFind = ip
        self._country = '-'
        self._city = '-'


    def findLocation(self):
        location = self._geodata.get_location(self._ipFind, detailed=True)
        self._country = location['info']['country']['name_en']
        self._city = location['info']['city']['name_en']

    def getCountry(self):
        return self._country

    def getCity(self):
        return self._city
