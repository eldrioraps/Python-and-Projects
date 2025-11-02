def employee_information(columns,eid,ename,address):
    return [{columns[0]: i, columns[1]: j, columns[2]: k} 
     for i, j, k in zip(eid, ename, address)]