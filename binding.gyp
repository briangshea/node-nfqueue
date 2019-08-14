{
  "targets": [
    {
      "target_name": "nfqueue_binding",
      "sources": [
        "src/node_nfqueue.cpp"
      ],
      "libraries": [
        "-lnetfilter_queue"
      ],
      "cflags": [
        "-fpermissive"
      ],
      "include_dirs" : [
        "<!(node -e \"require('nan')\")"
      ]
    },
    {
      "target_name": "nfqueue_package",
      "type": "none",
      "dependencies": [ "nfqueue_binding" ],
      "copies":
        [{ "destination": "./",
           "files": [ './build/Release/nfqueue_binding.node' ]
        }]
    }
  ]
}
