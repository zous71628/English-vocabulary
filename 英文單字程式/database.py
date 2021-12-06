import psycopg2
import os


class ConnectDatabase(object):
    # connect to database

    # env = os.environ.get("PYTHON_ENV")
    # if (env == "production"):
    DATABASE_URL = os.environ[
        "DATABASE_URL"] = "postgres://qsamrabatiyelo:433fedd48e84326c3db335406302d0af952e43a397e704e1272ec36b27f15d99@ec2-3-230-219-251.compute-1.amazonaws.com:5432/danc0iei9kn9ld"
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cur = conn.cursor()

    # else:
    # conn = psycopg2.connect(
    #     host="localhost",
    #     database="vocabulary",
    #     user="postgres",
    #     password="0000",
    #     port="5432"
    # )
    # cur = conn.cursor()

    def count_days(self) -> str: #計算有幾天
        self.cur.execute("SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = 'public'")
        rows = self.cur.fetchall()

        return "".join("%s" % i for i in rows)

    def review(self, day): #複習
        self.cur.execute("SELECT * FROM day{0};".format(day))
        rows = self.cur.fetchall()

        print(*rows, sep="\n")

    def count_id(self, day: int) -> str: #計算有多少ID
        self.cur.execute("SELECT COUNT(id) FROM day{0};".format(day))
        rows = self.cur.fetchall()

        return "".join("%s" % i for i in rows)

    def shuffle_voc(self, day: int, idcountlist: list) -> list: #打亂的ID印出單字
        rows = []
        for i in idcountlist:
            self.cur.execute("SELECT * FROM day%s WHERE id = %s", [day, i])
            rows += self.cur.fetchall()
            # f = "".join("{0}".format(j) for j in rows)
            # list(f)
        return rows

