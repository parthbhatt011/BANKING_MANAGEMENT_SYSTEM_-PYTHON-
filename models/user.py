class user:
    def __inti__ (self,id,name,email,password_hash,role,created_at):
        self.id = id
        self.name = name
        self.email = email
        self.password_hash = password_hash
        self.role = role
        self.created_at = created_at

    def __repr__(self):
        return f"<User id: {self.id} name: {self.name} email: {self.email} password_hash: {self.password_hash} role: {self.role}>"