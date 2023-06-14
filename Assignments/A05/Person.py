class Person:
    last_pid = 1
    all_persons = []
    def __init__(self, pid=None, name=None, last_name=None, gender=None, generation=None, byear=None, dyear=None, dage=None,
                 myear=None, mage=None, ptype=None, clan=None, spouse_id=None, parent_id1=None, parent_id2=None,
                 parent_node_id=None):
        self.pid = Person.last_pid
        Person.last_pid += 1
        self.name = name
        self.last_name = last_name
        self.gender = gender
        self.generation = generation
        self.byear = byear
        self.dyear = dyear
        self.dage = dage
        self.myear = myear
        self.mage = mage
        self.ptype = ptype
        self.clan = clan
        self.spouse_id = spouse_id
        self.parent_id1 = parent_id1
        self.parent_id2 = parent_id2
        self.all_persons.append(self)

    def __str__(self):
        return f"Person ID: {self.pid}\n" \
               f"Name: {self.name}\n" \
               f"Last Name: {self.last_name}\n" \
               f"Gender: {self.gender}\n" \
               f"Generation: {self.generation}\n" \
               f"Birth Year: {self.byear}\n" \
               f"Death Year: {self.dyear}\n" \
               f"Death Age: {self.dage}\n" \
               f"Marriage Year: {self.myear}\n" \
               f"Marriage Age: {self.mage}\n" \
               f"Person Type: {self.ptype}\n" \
               f"Clan: {self.clan}\n" \
               f"Spouse ID: {self.spouse_id}\n" \
               f"Parent ID 1: {self.parent_id1}\n" \
               f"Parent ID 2: {self.parent_id2}\n" \
               f"Parent Node ID: {self.parent_node_id}"
    @classmethod
    def get_person_by_id(self, person_id):
        # print(self.all_persons)
        for person in self.all_persons:
            if person.pid == person_id:
                return person
        return None


