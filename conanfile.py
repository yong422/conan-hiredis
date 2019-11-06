#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from conans import ConanFile, CMake, tools


class HiredisConan(ConanFile):
    name = "hiredis"
    version = "0.14.0"
    license = "BSD 3-Clause"
    author = "ykjo <yong422@nate.com>"
    url = "https://github.com/yong422/conan-hiredis"
    homepage = "https://github.com/redis/hiredis"
    description = "Hiredis is a minimalistic C client library for the Redis database."
    topics = ("conan", "hiredis", "redis", "redis-client", "c")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"


    _source_folder = "redis_source"
    _zip_name = "{}.zip".format(version)

    def source(self):
        """
        패키지의 소스코드 다운로드 및 압축 해제
        """
        # https://docs.conan.io/en/latest/reference/tools.html#tools-get
        tools.get("{}/archive/v{}.zip".format(self.homepage, self.version))
        os.rename("hiredis-{}".format(self.version), self._source_folder)

    def build(self):
        self.run("cd {} && make".format(self._source_folder))
        #cmake = CMake(self)
        #cmake.configure(source_folder=self._source_folder)
        #cmake.build()

    def package(self):
        self.copy("*.h", dst="include", keep_path=False)
        if self.options["shared"]:
            self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["hiredis"]
