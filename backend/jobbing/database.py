# from sqlalchemy import create_engine
# from sqlalchemy.orm import Session
# from jobbing import app

# engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=True)

# with Session(engine) as session:
#     result = session.execute("SELECT username from users")
#     print("TABLE users QUERY result:")
#     for row in result:
#         print("%s", row.username)