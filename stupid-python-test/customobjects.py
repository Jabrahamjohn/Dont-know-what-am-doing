class HAL9000(object):
    def __format__|(self, format):
        if (format == 'open-the-pod-bay-doors'):
            return "I'm afraid I can't do that."
        return 'HAL 9000'

'{:open-the-pod-bay-doors}'.format(HAL9000())
