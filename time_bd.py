import argparse

def process_text_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    total_time_SSMs = 0.0
    total_time_LLMs = 0.0

    in_block_SSMs = False
    in_block_LLMs = False
    is_request_manager_info = False

    for line in lines:
        if "SpecIncMultiHeadSelfAttention forward time" in line:
            in_block_SSMs = True
        elif "new_bc.num_tokens" in line:
            in_block_SSMs = False

        if "TreeIncMultiHeadSelfAttention forward time" in line:
            in_block_LLMs = True
        elif "RequestManager" in line:
            in_block_LLMs = False
            is_request_manager_info = True


        if not is_request_manager_info and (in_block_SSMs or in_block_LLMs):
            time_str = line.split('=')[-1].strip().replace("ms", "")
            time_val = float(time_str)
            if in_block_SSMs:
                total_time_SSMs += time_val
            if in_block_LLMs:
                total_time_LLMs += time_val

        is_request_manager_info = False

    return total_time_SSMs, total_time_LLMs

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process multiple text files.')
    parser.add_argument('file_paths', metavar='N', type=str, nargs='+',
                        help='a list of text files to be processed')
    
    args = parser.parse_args()

    for file_path in args.file_paths:
        total_time_SSMs, total_time_LLMs = process_text_file(file_path)
        print(f"For file {file_path}:")
        print(f"  Total time period for LLMslock SSMs: {total_time_SSMs}ms")
        print(f"  Total time period for LLMslock LLMs: {total_time_LLMs}ms")
