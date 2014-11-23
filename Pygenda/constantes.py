
class const:
    DB_PATH = "./DB/pygenda.db"
    APP_VERSION = "0.1.2"

    class sql:
        class persona:
            SELECT = "select * from Persona;"
            SELECT_BY_ID = "select * from Persona where id=?;"
            INSERT = "insert into Persona" \
                     " (Nombre, Apellidos, Fijo, ExtFijo, Movil, ExtMovil, Email, Departamento) " \
                     "values(?,?,?,?,?,?,?,?);"
            UPDATE = """
                        update Persona set
                        Nombre = ?,
                        Apellidos=?,
                        Fijo=?,
                        ExtFijo=?,
                        Movil=?,
                        ExtMovil=?,
                        Email=?,
                        Departamento=?
                        where id = ?;
                      """
            DELETE = """
                        delete from Persona where id =?;
                    """

        class departamento:
            SELECT = "select * from Departamentos;"
            INSERT = "insert into Departamentos (Nombre) values ('?');"
            DELETE = """
                    delete from Departamentos where Nombre = '?';
                    """
