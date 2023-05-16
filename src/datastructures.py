
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint
from utils import get_response_body



class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
                {
                    "id": self._generateId(),
                    "name": "John",
                    "last_name": "Jackson",
                    "age": "33",
                    "lucky_numbers":[7,13,22]
                },
                {
                    "id": self._generateId(),
                    "name": "Jane",
                    "last_name": "Jackson",
                    "age": "35",
                    "lucky_numbers":[10,14,3]
                },
                {
                    "id": self._generateId(),
                    "name": "Jimmy",
                    "last_name": "Jackson",
                    "age": "5",
                    "lucky_numbers":[1]
                }
            ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        self._members.append(member)
        return get_response_body(self._members,200)

    def delete_member(self, member_id):
        response = {}
        new_list = [member for member in self._members if member["id"]!=member_id]

        if new_list == self._members:
            response = get_response_body({"done":False},404)

        else:
            self._members = new_list
            response = get_response_body({"done":True},200) 

        return response

    def get_member(self, member_id):
        selected_member = [ member for member in self._members if member["id"]==member_id]
        response = {}

        if len(selected_member) == 0 :
            response = get_response_body({"done":False},404) 

        else:
            response = get_response_body({"result":selected_member[0]},200) 

        return response

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        response = get_response_body(self._members,200)        
        return response


