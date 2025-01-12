#Route Crypto Algorithm
def route_sifre_coz(encrypted_text: str, column_count: int, clockwise = True, starting_position = 1):  
    """
    This function decrypts a message that has been encrypted using the route cipher algorithm, based on the specified direction (clockwise or counter-clockwise).

    Parameters:

        encrypted_text (str): The encrypted message to be decrypted.

        column_count (int): The number of columns used in the route cipher algorithm.

        clockwise (bool, optional): The direction of the decryption process. If True, the decryption is performed in a clockwise direction. If False,
        it is performed counter-clockwise. Default is True.
        
        starting_position (int, optional): The starting position for the decryption process. The possible values are:
        1: Top-right corner
        2: Bottom-right corner
        3: Bottom-left corner
        4: Top-left corner
        Default is 1.

    Returns:
    str: The decrypted message.

    Raises:
    ValueError: If the length of the encrypted text is not divisible by the column count, or if the starting position is not one of the valid options (1, 2, 3, 4).
    """
    row_count = len(encrypted_text) // column_count
    if len(encrypted_text) % column_count != 0:
        raise ValueError("The length of the encrypted text must be divisible by the column count.")
    if starting_position not in (1, 2, 3, 4):
        raise ValueError("The starting position must be one of the following: 1, 2, 3, 4.")
    
    table = [['' for _ in range(column_count)] for _ in range(row_count)]
    if starting_position == 1:
        row_index= 0
        column_index= column_count -1
        direction_r_or_c = 0
        if clockwise:    
            row_direction=1
            column_direction = 1
            increase_row = -1
            increase_column = 1  
        else:
            row_direction= 0
            column_direction = 0
            increase_row = -1
            increase_column = 1  
    elif starting_position ==2:
        row_index= row_count -1
        column_index= column_count -1
        direction_r_or_c = 1

        if clockwise:
            row_direction=1
            column_direction = 0    
            increase_row = 1
            increase_column = 1  
        else:
            row_direction=0
            column_direction = 1    
            increase_row = 1
            increase_column = 1
    elif starting_position == 3:
        row_index= row_count -1
        column_index= 0
        direction_r_or_c = 0

        if clockwise:
            row_direction=0
            column_direction = 0    
            increase_row = 1
            increase_column = -1  
        else:
            row_direction= 1
            column_direction = 1    
            increase_row = 1
            increase_column = -1
    elif starting_position ==4:
        row_index= 0
        column_index= 0
        direction_r_or_c = 1

        if clockwise:
            row_direction=0
            column_direction = 1    
            increase_row = -1
            increase_column = -1  
        else:
            row_direction=1
            column_direction = 0   
            increase_row = -1
            increase_column = -1
    encrypted_text_index = 0
    last_column_index = column_count -1
    last_row_index = row_count -1
    initial_row_index = 0
    initial_column_index= 0
    rotate = True
    while encrypted_text_index < row_count*column_count:
        table[row_index][column_index] = encrypted_text[encrypted_text_index]
        encrypted_text_index  += 1
        print("******************")
        for rows in table:           
            print(rows)            
        print("******************")
        if rotate:
            if row_direction == 0 and row_index == initial_row_index and row_index != last_row_index:
                
                row_direction = 1
                initial_row_index += 1
                direction_r_or_c = 1
                increase_column *= -1
                
            elif column_direction == 0 and column_index == initial_column_index and column_index != last_column_index:
                
                column_direction = 1
                initial_column_index += 1
                direction_r_or_c = 0
                increase_row *= -1    
                
            elif row_direction == 1 and row_index == last_row_index and row_index != initial_row_index:
                
                row_direction = 0
                increase_column *= -1
                last_row_index -= 1
                direction_r_or_c = 1
                
            elif column_direction == 1 and column_index == last_column_index and column_index != initial_column_index:     
                column_direction = 0
                direction_r_or_c = 0
                increase_row *= -1
                last_column_index -= 1   
            if last_row_index == initial_row_index == row_index:
                direction_r_or_c = 1
                increase_column *= -1
                rotate = False
            if last_column_index == initial_column_index == column_index:
                direction_r_or_c = 0
                increase_row *= -1
                rotate = False 
        
        if direction_r_or_c == 0:
            row_index += increase_row
        if direction_r_or_c == 1:
            column_index += increase_column
        
    cozulmus_metin = ''
    for row in range(row_count):
        for column in range(column_count):
            cozulmus_metin += table[row][column]
    
    return cozulmus_metin

# route_encrypted_text = 'XRAASELLM'
# column_count = 3
# sonuc = route_sifre_coz(route_encrypted_text,column_count, True , 2)

route_encrypted_text = 'AİRERXXEDRANNVATÇEHEYNHİ'
column_count = 4
sonuc = route_sifre_coz(route_encrypted_text,column_count, True , 1)
print(sonuc)