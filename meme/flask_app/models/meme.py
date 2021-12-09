from flask_app.config.mysqlconnection import connectToMySQL

class Meme:
    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.meme_url = data["meme_url"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all_memes(cls):
        query = "SELECT * FROM memes ORDER BY id DESC"
        db_memes = connectToMySQL("memes_db").query_db(query)
        memes = []

        for meme in db_memes:
            memes.append(Meme(meme))

        return memes

    @classmethod
    def insert_meme(cls,data):
        query = "INSERT INTO memes (name,meme_url) VALUES (%(name)s,%(meme_url)s)"
        return connectToMySQL("memes_db").query_db(query,data)

    @classmethod
    def delete_meme(cls,data):
        query = "DELETE FROM memes WHERE id = %(id)s"
        return connectToMySQL("memes_db").query_db(query,data)

    @classmethod
    def get_meme(cls,data):
        query = "SELECT * FROM memes WHERE id = %(id)s"
        meme = connectToMySQL("memes_db").query_db(query,data)
        return cls(meme[0])

    @classmethod
    def edit_meme(cls,data):
        query = "UPDATE memes SET name=%(name)s, meme_url=%(meme_url)s WHERE id = %(id)s"
        return connectToMySQL("memes_db").query_db(query,data)

    