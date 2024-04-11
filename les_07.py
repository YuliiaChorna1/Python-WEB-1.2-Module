# Facade

class VideoFile:
    ...

class OggCompressionCodec:
    ...

class MPEG4CompressionCodec:
    ...

class CodecFactory:
    ...

class BitrateReader:
    ...

class AudioMixer:
    ...

class File:
    ...

class VideoConverter:
    def convert(filename, format):
        file = VideoFile(filename)
        sourceCodec = CodecFactory.extract(file)

        if (format == "mp4"):
            destinationCodec = MPEG4CompressionCodec()
        else:
            destinationCodec = OggCompressionCodec()

        buffer = BitrateReader.read(filename, sourceCodec)
        result = BitrateReader.convert(buffer, destinationCodec)
        result = AudioMixer().fix(result)
        return File(result)
    
convertor = VideoConverter()
mp4 = convertor.convert("funny-cats-video.ogg", "mp4")
mp4.save()