params.input_string = "Hello World"

process convertToUpper {
    input:
    val string from params.input_string

    output:
    stdout

    script:
    """
    echo \$string | tr 'a-z' 'A-Z'
    """
}

workflow {
    convertToUpper()
}
