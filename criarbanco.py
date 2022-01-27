import sqlite3

conexao = sqlite3.connect("EstoqueRes.db")
c = conexao.cursor()
c.execute(
            """
            create table if not exists usuarios(
                idusuario integer primary key autoincrement,
                nome text,
                usuario text,
                senha text
            )
            """
        )
c.execute(
            """
            create table if not exists produtos(
                idproduto integer primary key autoincrement,
                nome text,
                quantidade float,
                quantmin float,
                quantmax float

            )
            """
        )
conexao.commit()