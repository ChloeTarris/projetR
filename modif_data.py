import csv


KEYS_ALL = {'ASR_ID', 'CONTENTS', 'STATE', 'ORI', 'GROUP', 'DIV', 'AGHEADER', 'YEAR', 'MSA', 'COUNTY', 'SEQNO', 'SUB', 'CORE',
 'COVBY', 'POP', 'AGENCY', 'STNAME', 'MONTH', 'MOHEADER', 'BREAK', 'AREO', 'ZERO', 'DTLASTUP', 'DTPRUP1', 'DTPRUP2',
  'JUVDISP', 'JDHANDDP', 'JDREFJC', 'JDREFWA', 'JDREFOPA', 'JDREFCC', 'OFFENSE', 'OCCUR', 'M0_9', 'M10_12', 'M13_14',
   'M15', 'M16', 'M17', 'M18', 'M19', 'M20', 'M21', 'M22', 'M23', 'M24', 'M25_29', 'M30_34', 'M35_39', 'M40_44', 'M45_49', 'M50_54',
    'M55_59', 'M60_64', 'M65', 'F0_9', 'F10_12', 'F13_14', 'F15', 'F16', 'F17', 'F18', 'F19', 'F20', 'F21', 'F22', 'F23', 'F24',
     'F25_29', 'F30_34', 'F35_39', 'F40_44', 'F45_49', 'F50_54', 'F55_59', 'F60_64', 'F65', 'AW', 'AB', 'AI', 'AA', 'JW', 'JB',
      'JI', 'JA', 'AH', 'AN', 'JH', 'JN'
}

KEYS_IN = {'STNAME','COUNTY','YEAR','OFFENSE','M0_9','M10_12','M13_14','M15','M16',
                'M17','F0_9','F10_12','F13_14','F15','F16','F17','JW','JB','JI','JA','JH','JN'}

KEYS_OUT = KEYS_ALL - KEYS_IN

print(KEYS_OUT)

nbrs=[2,5,31,33,34,35,36,37,38,55,56,57,58,59,60,81,82,83,84,87,88]
with open('data/ICPSR_37056/DS0001/37056-0001-Data.tsv','r') as f:
        r=csv.DictReader(f, delimiter='\t')
        l=list(r)
print(l[0])
print(l[0]['JN'])
for d in l:
    for k in KEYS_OUT:
        d.pop(k)
           
with open('new_data.csv','w') as csvfile:
    writer=csv.DictWriter(csvfile,fieldnames=sorted(list(KEYS_IN)))
    writer.writeheader()
    for d in l:
        writer.writerow(d)

