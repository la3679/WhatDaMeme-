import os

def get_last_50_sentences_efficient(filename):
    sentences = []
    chunk_size = 4096  # Read in 4KB chunks
    
    with open(filename, 'r', encoding='utf-8') as file:
        # Move to end of file
        file.seek(0, 2)  # 2 means seek from end
        file_size = file.tell()
        
        # Read chunks from end until we have 50 sentences
        chunk_end = file_size
        while chunk_end > 0 and len(sentences) < 50:
            # Calculate chunk start
            chunk_start = max(chunk_end - chunk_size, 0)
            file.seek(chunk_start)
            
            # Read chunk
            chunk = file.read(chunk_end - chunk_start)
            
            # Split into sentences
            new_sentences = [s.strip() for s in chunk.replace('!', '.').replace('?', '.').split('.') if s.strip()]
            sentences = new_sentences + sentences
            
            chunk_end = chunk_start
            
        # Return last 50 sentences
        return sentences[-50:] if len(sentences) >= 50 else sentences