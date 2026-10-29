rule lab_hello_banner
{
    meta:
        author = "Gitsimbanyi Prosper"
        description = "Benign reverse-engineering-labs sample banner"
        sample = "lab_hello.c"
    strings:
        $a = "LAB-HELLO-BANNER" ascii
        $b = "reverse-engineering-labs: authorized benign sample" ascii
    condition:
        all of them
}
