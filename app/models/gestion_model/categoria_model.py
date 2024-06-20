import sqlite3
import logging
from app.models.database import create_connection

class CategoriaModel:

    ####################### CRUD #######################

    @staticmethod
    def create_categoria(nombre_categoria):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO Categoria (nombre_categoria)
                VALUES (?)
            ''', (nombre_categoria,))
            conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            logging.error(f"Error al crear categoría: {e}")
        finally:
            conn.close()

    @staticmethod
    def read_categoria(id_categoria):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Categoria WHERE id_categoria = ?", (id_categoria,))
            return cursor.fetchone()
        except sqlite3.Error as e:
            logging.error(f"Error al leer categoría: {e}")
        finally:
            conn.close()

    @staticmethod
    def update_categoria(id_categoria, nombre_categoria):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE Categoria 
                SET nombre_categoria = ?
                WHERE id_categoria = ?
            ''', (nombre_categoria, id_categoria))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error al actualizar categoría: {e}")
        finally:
            conn.close()

    @staticmethod
    def delete_categoria(id_categoria):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Categoria WHERE id_categoria = ?", (id_categoria,))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error al eliminar categoría: {e}")
        finally:
            conn.close()

    ####################### OTROS BÁSICOS #######################
    
    @staticmethod
    def list_all_categorias():
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Categoria")
            return cursor.fetchall()
        except sqlite3.Error as e:
            logging.error(f"Error al listar categorías: {e}")
        finally:
            conn.close()
