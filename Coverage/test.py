def block_coverage(G,input_test_cases,Blocks_and_Conditions,num_testcases,Testcases_Blocks_Coverage):
    statements_covered = []
    
    def traverse(node,testcase_id,blocks_covered,Dict_of_Branches,explore):
    # Evaluate the condition using the input test cases
        conditions = node.cond
        if node.cond is not None:
            final_result = True
            if explore:
                for condition in node.cond:
                    if len(condition) == 3:
                        result = evaluate_condition(condition[1],condition[2], input_test_cases, testcase_id)
                    else:
                        result = evaluate_condition(condition[1],None, input_test_cases, testcase_id)
                    if condition[0] == 0: # else statements so condition is inverted
                        result = not result
                    final_result = final_result and result
            else:
                final_result = False
        else:
            final_result = True # Block has no condition

        # Build Blocks_and_Conditions dict, it is testcase independent so do it only once
        if testcase_id == 0:
            Blocks_and_Conditions[node.block_id] = conditions
            if final_result: # always True
                Dict_of_Branches.update({node.block_id:(2, node.all_conds)}) 
            else: # always False
                Dict_of_Branches.update({node.block_id:(1, node.all_conds)}) 
        else:
            ## update Dict_of_Branches
            pass


        print("Testcase: ", testcase_id," Block ID: ",node.block_id, " Condition result:", final_result,"\n")


        if final_result is True: # If the block is covered increment blocks covered and mark its statements as covered
            blocks_covered += 1
            statements_covered.extend(node.statements_list)

            # Dictionary were keys are testcases and values are list of blocks the testcase covers
            if testcase_id in Testcases_Blocks_Coverage:
                Testcases_Blocks_Coverage[testcase_id].append(node.block_id)
            else:
                Testcases_Blocks_Coverage[testcase_id] = [node.block_id]

            # Traverse children only if the final result is True
            for child in G.successors(node):
                blocks_covered,Dict_of_Branches = traverse(child,testcase_id,blocks_covered,Dict_of_Branches,explore=True)
        else:
            for child in G.successors(node):
                blocks_covered,Dict_of_Branches = traverse(child,testcase_id,blocks_covered,Dict_of_Branches,explore=False)
        return blocks_covered,Dict_of_Branches
    
    root = get_root(G)
    Dict_of_Branches = dict()
    for testcase_id in range(num_testcases):
        blocks_covered = 0
        blocks_covered,Dict_of_Branches = traverse(root,testcase_id,blocks_covered,Dict_of_Branches,explore=True)
        blocks_covered -= 1 
        if testcase_id == 0:
            Dict_of_Branches.pop(0)
            #print("Dictionary of branches",Dict_of_Branches)
            total_blocks = len(Blocks_and_Conditions)-1
            #print("Total blocks = ", total_blocks)
        percentage_covered = (blocks_covered / total_blocks) * 100
        #print("Tescase ", testcase_id, " Blocks Covered ", blocks_covered, " Percentage block coverage", percentage_covered)
        #print("\n")
    #print(Testcases_Blocks_Coverage)
    #traverse(root,explore=True)
    #print("Statements Covered: ",statements_covered)
    return Dict_of_Branches