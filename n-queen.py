import random

n = 8
n_queens = n
no_attempts = 0
win = False
chess_board = [["E" for x in range(n)] for i in range(n)]

def view_board(chess_board):

	for x in range(0, n):
		for y in range(0, n):
			print(chess_board[x][y], end=' ')
		print()

 
def place_queens(n_queens, chess_board):
	chess_board = [["E" for x in range(n)] for i in range(n)]

	queen = "Q"
	counter = 0
	while counter != 8:
		outer_choice = random.choice(range(0, len(chess_board)))
		choice = random.choice(range(0, len(chess_board[outer_choice])))
		if chess_board[outer_choice][choice] != "Q": 
			counter += 1
			chess_board[outer_choice][choice] = queen
	return chess_board

def flatten(chess_board):
	i = 1
	flattened_list = []
	for x in chess_board:
		for y in x:
			flattened_list.append(i)
			i += 1

	return flattened_list


def directions(q_index_out, q_index_in, chess_board):
	up = []
	down = []
	left = []
	right = []
	diagonal_left = []
	diagonal_right = []
	
	# for loop to find left
	if q_index_in != 0:
		
		for x in range(q_index_in):

			left.append([q_index_out, x])

	
	# for loop to find right
	
	for x in range(q_index_in + 1, len(chess_board)):
		if q_index_in == len(chess_board[q_index_out]) - 1:
			break
		else:
			right.append([q_index_out, x])

	# for loop to find up

	for x in range(0, q_index_out):
		if q_index_out == 0:
			break
		else:
			up.append([x, q_index_in])


    # for loop to find down

	for x in range(q_index_out + 1, len(chess_board)):
		if q_index_out == len(chess_board):
			break
		else:
			down.append([x, q_index_in])

	# for loop to find diagonal left

	
	if q_index_out == 0:
		if q_index_in != 0:
			# no_elements = pow(len(chess_board), 2)
			value = q_index_in - 1
			for y in range(q_index_out + 1, len(chess_board)):
				
				diagonal_left.append([y, value])
				value -= 1
				if value < 0:
					break


	else:
		if q_index_in != 0:
			if q_index_in != len(chess_board) - 1:
				value = q_index_in + 1
				for x in reversed(range(0, q_index_out)):

					diagonal_left.append([x, value])
					value += 1
					if value > len(chess_board) - 1:
						break

			if q_index_out != len(chess_board) - 1:
				value = q_index_in - 1

				for y in range(q_index_out + 1, len(chess_board)):

					diagonal_left.append([y, value])
					value -= 1
					if value < 0:
						break
		else:
			value = q_index_in + 1
			for x in reversed(range(0, q_index_out)):
				diagonal_left.append([x, value])


			



	#for loop to find diagonal right


	if q_index_out == 0:
		if q_index_in != len(chess_board) - 1:
			value = q_index_in + 1
			for y in range(q_index_out + 1, len(chess_board)):
				diagonal_right.append([y, value])
				value += 1

				if value > len(chess_board) - 1:
					break
		
	else:
		if q_index_in != len(chess_board) - 1:
			value = q_index_in + 1
			for y in range(q_index_out + 1, len(chess_board)):
				diagonal_right.append([y, value])
				value += 1

				if value > len(chess_board) - 1:
					break
			
		
		value = q_index_in - 1
		for y in reversed(range(0, q_index_out)):
			diagonal_right.append([y, value])
			value -= 1
			if value < 0:
				break

			

	direction = [up, down, right, left, diagonal_right, diagonal_left]
	return direction

def check(chess_board, array_list = []):
    position = None

    for x in array_list:
       a = x[0]
       b = x[1]
       position = chess_board[a][b]
       if position == "Q":
           return True
       else:
           continue



def check_conflict(chess_board, direction, q_index_outer,  q_index_inner):


	flag = False
	for x in direction:

		flag = check(chess_board, x)
		if flag == True:

   			return True
		else:
   			continue


		

def is_conflict(chess_board):
	outer_index = 0
	conflict = 0
	for x in chess_board:

		for y in x:

			if y == "Q":

				q_index = x.index(y)
				direction = directions(outer_index, q_index, chess_board)
				# direction = [x for x in direction if x]
				has_conflict = check_conflict(chess_board, direction, outer_index, q_index)
				if has_conflict:
					conflict += 1
		outer_index += 1


	
	return conflict




while win == False:
	no_attempts += 1
	chess_board = place_queens(n_queens, chess_board)
	conflict = is_conflict(chess_board)
	if conflict == 0:
		win = True
	else:
		if no_attempts == 10000:
			print("10000 times attempted !!!")
			print("No result is found !!!")
			break
		print("Attempt number:" + str(no_attempts))
		view_board(chess_board)
		print("Conflicts number: " + str(conflict))

else:
	print("Congratulations !!!")
	print("Solution is found !!!")
	view_board(chess_board)
	print("Total attempts: " + str(no_attempts))
	print("Conflict: " + str(conflict))

 
