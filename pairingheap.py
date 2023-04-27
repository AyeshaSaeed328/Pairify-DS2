import csv

symptoms_dict = dict()
with open("project file 2.csv", 'r') as file:
    symptoms_file = csv.reader(file)
    next(symptoms_file)
    for symptoms,priority in symptoms_file:
        symptoms_dict[symptoms] = priority #{symptom: priority}

class Patient():
    def __init__(self, name, age, symptoms, id = 0) -> None:
        self.id = id
        self.name = name
        self.age = age
        self.symptoms_str = symptoms
        self.symptoms = symptoms.split(", ")
        self.priority = self.calculate_priority(self.symptoms)
    
    def calculate_priority(self, symptoms_lst: list) -> int:
        priority = 0
        for symptom in symptoms_lst:
            priority += int(symptoms_dict[symptom]) #for every symptom, adds its priority in patients priority
        return priority
    
    def update_symptoms(self, symptoms_lst:str):
        self.symptoms_str = symptoms_lst
        self.symptoms = symptoms_lst.split(", ")
        self.priority = self.calculate_priority(self.symptoms)
    

class Node():
    def __init__(self, patient:Patient = None):
        self.sibling_after = None
        self.child = None
        self.sibling_before = None
        self.parent = None
        self.patient:Patient = patient

        
class PairingHeap():
    def __init__(self):
        self.root:Node = None #initializing a heap with root none
        self.inserts = 0

    def MakeHeap(self, key:Patient): #makes a new Node having the value equal to the given key
        new_root = Node(key)
        return new_root #returns the root of the node

    def insert(self, key:Patient):
        if self.root == None: #if this is the first node to insert then make a new heap and make it the root of the heap
            self.root = self.MakeHeap(key)
        else:
            new_root = self.MakeHeap(key)  #if the heap is not empty then create a new heap with the new key value
            self.root = self.Merge(self.root, new_root) #merge the already existing hep with the new created one
        
    def Merge(self, heap1:Node, heap2:Node):#takes the roots of both heaps; only roots because only the pointers of the root need to be changed
        if heap1 is None:
            return heap2
        if heap2 is None:
            return heap1
        if heap2.patient.priority > heap1.patient.priority: #to make sure that heap1 is the heap with maximum value; this makes further execution easy
            heap1, heap2 = heap2, heap1
        #updating the pointers; 
        if heap1.child:
            heap1.child.sibling_before = heap2
        heap2.sibling_after = heap1.child
        heap1.child = heap2
        heap2.parent = heap1
        heap1.sibling_after = None
        heap1.sibling_before = None
        self.root = heap1
        return self.root

    def FindMax(self): #Returns the patient with heighest priority, doesnot remove it
        return (self.root.patient.id, self.root.patient.name, self.root.patient.age, self.root.patient.symptoms)

    def deleteMax(self):
        deleting = self.root
        children = []
        temp = self.root.child
        children.append(temp)
        while temp.sibling_after is not None:
            temp = temp.sibling_after
            children.append(temp)
        self.root = self.double_merge(children)
        return deleting
 
    def double_merge(self, lst):
        if len(lst) == 1:
            return lst[0]
        elif len(lst) == 2:
            return self.Merge(lst[0], lst[1])
        else:
            return self.Merge(self.Merge(lst[0], lst[1]), self.double_merge(lst[2:]))

    def find(self, id):
        node = self.root
        if node.patient.id == id:
            return node
        while node.child is not None:
            node = node.child
            if node.patient.id == id:
                return node
            while node.sibling_after is not None:
                node = node.sibling_after
                if node.patient.id == id:
                    return node
        return None
    
    def update(self, id, name = "", age = "", symptoms = ""):
        patient_node = self.find(id)
        to_return = patient_node.patient
        if patient_node is not None:
            if symptoms != "":
                patient_node.patient.update_symptoms(symptoms)
            if age != "":
                patient_node.patient.age = age
            if name != "":
                patient_node.patient.name = name

            if patient_node == self.root:
                children = []
                temp = self.root.child
                children.append(temp)
                while temp.sibling_after is not None:
                    temp = temp.sibling_after
                    children.append(temp)
                self.root.child = None
                self.root = self.double_merge(children)

            elif patient_node.parent:
                patient_node.parent.child = patient_node.sibling_after
                if patient_node.sibling_after:
                    patient_node.sibling_after.parent = patient_node.parent
                patient_node.parent = None
            else:
                patient_node.sibling_after.sibling_before = patient_node.sibling_before
                patient_node.sibling_before.sibling_after = patient_node.sibling_after
            
            self.Merge(self.root, patient_node)
            return to_return
        return None

    def display_node(self,node:Node): 
        if not node:
            return self.all_q
        self.all_q.append(node.patient)
        if node.child:
            self.display_node(node.child)
        if node.sibling_after:
            self.display_node(node.sibling_after)
        
    def display(self):
        if not self.root:
            return
        self.all_q = []
        self.display_node(self.root)
        return (self.all_q)
        
patient_heap = PairingHeap()
with open("project file 1 (1).csv", 'r') as file:
    patients_file = csv.reader(file)
    next(patients_file)
    for name, age, symptoms in patients_file:
        patient_heap.inserts += 1
        new_patient = Patient(name, age, symptoms, patient_heap.inserts) #for every line, a new patient object is created and appended in a lst
        patient_heap.insert(new_patient)
