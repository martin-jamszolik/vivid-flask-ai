from flask import jsonify, current_app, request
from flask_restful import Resource, reqparse
from .models import Proposal, Task, proposals
from .ai import ProposalAIService


parser = reqparse.RequestParser()
parser.add_argument('location', type=str, required=True, help='Location cannot be blank')
parser.add_argument('tasks', type=list, required=True, help='Tasks cannot be blank')

class ProposalList(Resource):
    def get(self):
        #service = ProposalAIService(current_app.config)
        #service.ask_question("This is a basic test")       
        return jsonify([p.serialize() for p in proposals])

    def post(self):
        data = parser.parse_args()
        proposal = Proposal(location=data['location'])
        for task_data in data['tasks']:
            task = Task(name=task_data['name'], quantity=task_data['quantity'], price=task_data['price'])
            proposal.tasks.append(task)
        return proposal.serialize(), 201

class ProposalDetail(Resource):
    def get(self, id):
        proposal = proposals[id]
        return proposal.serialize()

    def put(self, id):
        proposal = proposals[id]
        data = parser.parse_args()
        proposal.location = data['location']
        proposal.tasks = []
        for task_data in data['tasks']:
            task = Task(name=task_data['name'], quantity=task_data['quantity'], price=task_data['price'])
            proposal.tasks.append(task)
        return proposal.serialize()

    def delete(self, id):
        return '', 204

