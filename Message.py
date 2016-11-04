class Message(object):

        class Status:
                New = 'E0001'
                InProgress = 'E0002'
                OnHold = 'E0003'
                CustomerAction = 'E0004'
                SolutionProvided = 'E0005'

        class Priority:
                Medium = 5
                High = 3


        def __init__(self, id, messageNo, description, statusId, priorityId, createdOn, changedOn, irtExpiration, mptExpiration, processorId, processorName, url, category):
                self.id             = id
                self.messageNo      = messageNo
                self.description    = description
                self.statusId       = statusId
                self.priorityId     = priorityId
                self.createdOn      = createdOn
                self.changedOn      = changedOn
                self.irtExpiration  = irtExpiration
                self.mptExpiration  = mptExpiration
                self.processorId    = processorId
                self.processorName  = processorName
                self.url            = url
                self.category       = category

        def requiresAction(self):
                #if self.statusId == Message.Status.New or self.statusId == Message.Status.InProgress:
                if self.statusId == Message.Status.New:
                        return True
                else:
                        return False

