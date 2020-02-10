import fire


class PgOnlineSchemaMigrate(object):
    def migrate(self, alter, table, database,
                    port=5432,
                    host='127.0.0.1',
                    username='',
                    password=''):
        print(alter)


if __name__ == "__main__":
    fire.Fire(PgOnlineSchemaMigrate)