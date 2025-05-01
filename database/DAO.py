from database.DB_connect import DBConnect
from model.aeroporto import Aeroporto
from model.rotta import Rotta
from model.volo import Volo


class DAO():

    @staticmethod
    def getAllAeroporti():
        conn = DBConnect.get_connection()

        result = {}

        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM airports"
        cursor.execute(query)

        for row in cursor:
            result[row["ID"]] = (Aeroporto(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdges():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM flights f"
        cursor.execute(query)

        for row in cursor:
            result.append(Volo(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getRotte():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select f.ORIGIN_AIRPORT_ID , f.DESTINATION_AIRPORT_ID , f.DISTANCE, count(*) as voli
                    from flights f 
                    group by f.ORIGIN_AIRPORT_ID , f.DESTINATION_AIRPORT_ID , f.DISTANCE"""

        cursor.execute(query)

        #rows = cursor.fetchall()

        for row in cursor:
            rotta = Rotta(
                aeroporto1= row["ORIGIN_AIRPORT_ID"],
                aeroporto2=row["DESTINATION_AIRPORT_ID"],
                distanza=row["DISTANCE"],
                numVoli=row["voli"]
            )
            result.append(rotta)
        cursor.close()
        conn.close()
        return result