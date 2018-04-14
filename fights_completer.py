from collections import defaultdict


class Boxer_Completion:
    def __init__(self,fights_file,schema):
        self.boxing_data =fights_file 
        self.boxers = defaultdict(dict)
        self.schema = schema
        #the schema should be a dictionary from category to first index in
        # so for example {'age':3}

    def fill_in(self,fight,boxer):
        pass 
    def boxer_stat(self):
        with open(self.boxing_data) as fights:
            for fight in fights:
               fight = fight.split('\t')
               boxer_left = self.boxers[fight[2]]
               boxer_right = self.boxers[fight[3]]
               for x in ['reach','height','stance']:
                   if fight[self.schema[x]] == 'None':
                       pass
                   elif x in boxer_left:
                       boxer_left[x].append(fight[self.schema[x]])
                   else:
                       boxer_left[x] = [fight[self.schema[x]]]
                   if fight[self.schema[x]+1] == 'None':   
                       pass
                   elif x in boxer_right:
                       boxer_right[x].append(fight[self.schema[x]+1])
                   else:
                       boxer_right[x] = [fight[self.schema[x]+1]]
               if (fight[self.schema['date']] == 'None' or
                    fight[self.schema['age']] == 'None') :
                   pass
               elif 'birth_year' in boxer_left:
                   year = (int(fight[self.schema['date']][0:4]) -
                                int(fight[self.schema['age']]))
                   boxer_left['birth_year'].append(str(year))
               else:                      
                   year= (int(fight[self.schema['date']][0:4]) -
                                int(fight[self.schema['age']]))
                   boxer_left['birth_year'] = [str(year)]
               if (fight[self.schema['date']] == 'None' or
                    fight[self.schema['age']+1] == 'None'):
                   pass
               elif 'birth_year' in boxer_right:
                   year = (int(fight[self.schema['date']][0:4]) -
                                int(fight[self.schema['age']+1]))
                   boxer_right['birth_year'].append(str(year))
               else:                      
                   year= (int(fight[self.schema['date']][0:4]) -
                                int(fight[self.schema['age']+1]))
                   boxer_right['birth_year'] = [str(year)]
        
        for x in self.boxers:
            boxer = self.boxers[x]
            for y in boxer:
                if y  != 'stance':
                    boxer[y] = str(sum(map(lambda x: int(x),boxer[y]))//\
                    len(boxer[y]))
                else:
                    boxer[y] = boxer[y][-1]
                
    def write_to_file(self,writing_file):
        fights = open(self.boxing_data, 'r')
        with open(writing_file, 'w') as writing:
            for line in fights:
                line = line.split('\t')
                for y in ['reach','height','stance']:
                    if line[self.schema[y]] == 'None' and y in self.boxers[line[2]]:
                        line[self.schema[y]] = self.boxers[line[2]][y]
                    if line[self.schema[y]+1] == 'None' and y in self.boxers[line[3]]:
                        line[self.schema[y]+1] = self.boxers[line[3]][y]
                for x in line:
                    writing.write(x + '\t')
                writing.write('\n')
