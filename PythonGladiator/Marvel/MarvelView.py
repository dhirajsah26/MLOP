import Connection.PGConn as PGConn

class MarvelView:
    conn = PGConn.DBConnector()

    def get_view(self):
        self.conn.display_marvel()
