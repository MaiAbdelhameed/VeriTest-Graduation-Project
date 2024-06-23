# make absolute path function

make_absolute_path() {
    local path="$1"
    if [[ "${path:0:1}" != "/" ]]; then
        path="$(pwd)/$path"  # prepend current directory
    fi
    echo "$path"
}

# run main python file
# Check if argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <file_path>"
    exit 1
fi

file_path="$1"
absolute_path=$(make_absolute_path "$file_path")

echo ABSOLUTE 
echo $absolute_path
cp "$file_path" "$VERITEST_HOME/PARSER/files"

python "$VERITEST_HOME"/main.py "$(basename "$absolute_path")"

echo "generated test cases file"

cp "$VERITEST_HOME"/output/output_file.txt "$VERITEST_HOME/output_generator"

# golden model path
golden_model="${absolute_path%.*}.py"

# copy golden model
cp "$golden_model" "$VERITEST_HOME/output_generator"
# copy verilog code
cp "$absolute_path" "$VERITEST_HOME/output_generator"


python "$VERITEST_HOME/output_generator/genertor.py" "$VERITEST_HOME/output_generator/output_file.txt"

# remove excess files
model_name=$(basename "$absolute_path")
model_name_no_extension="${model_name%.*}"
rm "$VERITEST_HOME/output_generator/${model_name_no_extension%.*}.py"
rm "$VERITEST_HOME/output_generator/${model_name_no_extension%.*}.v"
rm "$VERITEST_HOME/output_generator/output_file.txt"
