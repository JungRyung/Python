skill = 'CBD'
skill_trees = ['BACDE','CBADF','AECB','BDA']

def solution(skill, skill_trees):
	answer = 0
	SW=0
	print(skill[0])
	for skill_trees_element in skill_trees:
		skill_cnt=0
		for sk_idx,sk in enumerate(skill_trees_element):
			if(SW):
				SW=0
				break
			for skill_element in skill:
				print('%s , %s\tsk_idx : %d\n'%(sk,skill_element,sk_idx))
				if(sk==skill_element):
					if(sk==skill[skill_cnt]):
						skill_cnt = skill_cnt + 1
						print("coincide")
						print("skill_cnt : %d\n"%(skill_cnt))
						break
					else:
						print("break")
						SW=1
						break
			if(sk_idx+1==len(skill_trees_element)):
				answer = answer + 1
				print('answer : %d'%(answer))


	return answer

answer = solution(skill, skill_trees)
print(answer)
