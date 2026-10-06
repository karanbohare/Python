import mysql.connector
from app.models.policy import Policy

class PolicyRepository:
   
    def __init__(self):
         self.connection =mysql.connector.connect(**database_config)
    self._policies = {
        1: Policy(id=1,name="Jeevan Labh",description="Life insurance savings plan",maturity="10 years",premium=15000.0),
        2: Policy(id=2,name="Jeevan Arogya",description="Health insurance plan",maturity="5 years",premium=12000.0),
        3: Policy(id=3,name="Jeevan Suraksha",description="Family protection plan", maturity="15 years",premium=20000.0 )
                    }
        
    self._next_id=4
    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM policies")
        rows = cursor.fetchall()
        return [Policy(*row) for row in rows]

    def get_by_id(self, policy_id:int):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM policies WHERE id = %s", (policy_id,))
        row = cursor.fetchone()
        return Policy(*row) if row else None

    def create(self, policy_data:dict):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO policies (name, description, maturity, premium) VALUES (%s, %s, %s, %s)", 
                       (policy_data['name'], policy_data['description'], policy_data['maturity'], policy_data['premium']))
        self.connection.commit()
        policy_id = cursor.lastrowid
        return self.get_by_id(policy_id)

    def update(self, policy_id: int, policy_data: dict):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE policies SET name=%s, description=%s, maturity=%s, premium=%s WHERE id=%s",
                       (policy_data['name'], policy_data['description'], policy_data['maturity'], policy_data['premium'], policy_id))
        self.connection.commit()
        return self.get_by_id(policy_id)

    def delete(self, policy_id: int):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM policies WHERE id=%s", (policy_id,))
        self.connection.commit()
        return cursor.rowcount > 0