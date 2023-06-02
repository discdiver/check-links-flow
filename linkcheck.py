from prefect import flow
from prefect_shell import ShellOperation


@flow(log_prints=True)
def check_links():
    """Check the internal links for Prefect's documentation."""

    res = ShellOperation(commands=["linkchecker https://docs.prefect.io"]).run()
    print(res[8:])


if __name__ == "__main__":
    check_links()


# Scratchpad
# # for long running operations, you can use a context manager
# with ShellOperation(
#     commands=[
#         "linkchecker https://example.com",
#     ],
# ) as check_links_operation:
#     # trigger runs the process in the background
#     checker = check_links_operation.trigger()
#     checker.wait_for_completion()
#     # if you'd like to get the output lines, you can use the `fetch_result` method
#     # output_lines = checker.fetch_result()
#     # print(output_lines)


# # to put in Dockerfile above Prefefect
# # bash script
# # run the script

# # install Rust and dependencies on APT/dpkg-based Linux distros
# curl -sSf 'https://sh.rustup.rs' | sh
# apt install gcc pkg-config libc6-dev libssl-dev

# # install lychee
# cargo install lychee

# # check links on prefect docs
# lychee https://docs.prefect.io

# # send results to what - a Markdown file that gets read by Prefect into an Artifact
# # or has a link that points to a file in an S3 bucket
