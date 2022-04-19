from datetime import datetime

agentProfiles = [
            {
                'timestamp': datetime.now().timestamp(),
                'name': 'Ramesh Kumar',
                'agent_id': 1,
                'member since': '16-04-2022',
                'Supervisor': 'Kishan Raj',
                'Good delivery': 180,
                'Bad delivery': 70,
                'Reputation': ((180)/(180+70))*100,
                'digital signature': 'approved',
                'flagged': 'N'
            },
            {
                'timestamp': datetime.now().timestamp(),
                'name': 'Suresh Kumar',
                'agent_id': 2,
                'member since': '16-04-2022',
                'Supervisor': 'Paresh Raj',
                'Good delivery': 40,
                'Bad delivery': 50,
                'Reputation': ((40)/(40+50))*100,
                'digital signature': 'Not approved',
                'flagged': 'Y'
            },
            {
                'timestamp': datetime.now().timestamp(),
                'name': 'Harsh Choudhary',
                'agent_id': 3,
                'member since': '16-04-2022',
                'Supervisor': 'Kishan Raj',
                'Good delivery': 150,
                'Bad delivery': 50,
                'Reputation': ((150)/(150+50))*100,
                'digital signature': 'approved',
                'flagged': 'N'
            },
        ]