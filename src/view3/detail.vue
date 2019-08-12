<template>
    <el-container>
        <div class="page-main">
            <header class="page-header">
                <div class="page-header-back">
                    <i class="el-icon-arrow-left"></i>
                    <a @click="handle().back()">返回</a>
                </div>
                <div class="page-header-title">{{ this.$route.meta.title }}</div>
                <div class="page-header-next"></div>
            </header>
            <div class="page-content">
                <div class="page-content-form">
                    <el-form :ref="formName" :model="form" label-width="150px" size="small" :disabled="editType == 'detail'">
                        <el-form-item label="输入_31" prop="field_31" :rules="FormValid.required">
                            <el-input class="input-show-word" v-model="form.field_31" placeholder="输入提示_31" maxlength="50" show-word-limit></el-input>
                        </el-form-item>
                        <el-form-item label="">
                            <el-button :disabled="isSubmitting" type="primary" @click="handle().submit()" v-if="editType == 'add'">添加</el-button>
                            <el-button :disabled="isSubmitting" type="primary" @click="handle().submit()" v-if="editType == 'edit'">修改</el-button>
                        </el-form-item>
                    </el-form>
                </div>
            </div>
        </div>
    </el-container>
</template>