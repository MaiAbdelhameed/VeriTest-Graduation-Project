
# make absolute path function

make_absolute_path() {
    local path="$1"
    if [[ "${path:0:1}" != "/" ]]; then
        path="$(pwd)/$path"  # prepend current directory
    fi
    echo "$path"
}


# Check if argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <file_path>"
    exit 1
fi


# read verilog and json file

file_path="$1"
# absolute_path=$(make_absolute_path "$file_path")
# TODO: edit to make it run from any place
absolute_path="$VERITEST_HOME/web_portal/backend/uploaded_files/$file_path"
filename_without_extension=${absolute_path%.*}




# generate golden model
python "$VERITEST_HOME/Mode_2/main.py" "${filename_without_extension}.json"

# generate verilog TestBench file and run it from mode 1

bash "$VERITEST_HOME/main.sh" "${filename_without_extension}.v"
