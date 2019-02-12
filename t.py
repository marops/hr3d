#!/bin/bash
djm migrate issues zero
djm migrate issues
djm loaddata issues_initial.json
